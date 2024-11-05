import streamlit as st
from hand_estimation import HandEstimation
import cv2 as cv
from models.Recipe import Recipe
import time

class RecipePage:
    # Define font size variables
    TITLE_FONT_SIZE = "2.2em"
    DESCRIPTION_FONT_SIZE = "1.5em"
    SECTION_TITLE_FONT_SIZE = "2.5em"
    COMPONENT_FONT_SIZE = "1.5em"
    INGREDIENT_FONT_SIZE = "1.2em"
    STEP_FONT_SIZE = "1.5em"
    INFO_LABEL_FONT_SIZE = "1.3em"
    INFO_VALUE_FONT_SIZE = "1.3em"

    def __init__(self, recipe: Recipe):
        self.detector = HandEstimation()
        self.cap = cv.VideoCapture(0)
        self.recipe = recipe
        self.step = None
        self.current_step = 0
        
        # Initialize session state for managing video feed
        if "video_running" not in st.session_state:
            st.session_state.video_running = False
        if "recipe_page" not in st.session_state:
            st.session_state.recipe_page = None
    
    def display_title_and_description(self):
        st.markdown(
            f"""
            <div style="padding: 15px; background-color: #333333; border-radius: 8px;">
                <h1 style="color: #FFFFFF; font-weight: bold; font-size: {self.TITLE_FONT_SIZE};">{self.recipe.title}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            f"""
            <div style="background-color: #FFFFFF;padding: 15px; margin-top: 20px; border-radius:8px;">
                <p style="font-size: {self.DESCRIPTION_FONT_SIZE}; color: #333333;">{self.recipe.description}</p>
            </div>  
            """,
            unsafe_allow_html=True
        )
    
    def display_ingredients(self):
        st.markdown(
            f"""
            <div style="padding: 15px; background-color: #333333; border-radius: 8px; margin-bottom: 20px;">
                <h2 style="color: #FFFFFF; font-weight: bold; font-size: {self.SECTION_TITLE_FONT_SIZE};">Ingredients:</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
        for component in self.recipe.recipe_components:
            st.markdown(
                f"""
                <div style="padding: 5px; margin-left: 15px;">
                    <p style="font-size: {self.COMPONENT_FONT_SIZE}; font-weight: bold; color: #FFA726;">{component.name}</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            for ingredient in component.ingredients_per_portion:
                st.markdown(
                    f"""
                    <div style="margin-left: 30px; color: #FFFFFF; font-size: {self.INGREDIENT_FONT_SIZE};">
                        - {ingredient.name}: {ingredient.amount_per_portion} {ingredient.measurement_type}
                    </div>
                    """, 
                    unsafe_allow_html=True
                )

    def display_current_step(self):
        current_step = self.recipe.steps[self.current_step]

        # Split the description into sentences and format each as a bullet point
        description_sentences = current_step.description.split('.')
        formatted_description = "".join(
            f"<li style='margin-bottom: 8px;'>{sentence.strip()}</li>" 
            for sentence in description_sentences if sentence.strip()
        )

        self.step.markdown(
            f"""
            <div style="padding: 15px; background-color: #333333; border-radius: 8px;">
                <h2 style="color: #FFFFFF; font-weight: bold; font-size: {self.SECTION_TITLE_FONT_SIZE};">
                    Step {current_step.number}
                </h2>
            </div>
            <div style="padding: 15px; background-color: #FFFFFF; border-radius: 8px; margin-top: 20px;">
                <ul style="font-size: {self.STEP_FONT_SIZE}; color: #333333;">
                    {formatted_description}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

        
    
    def display_time_and_difficulty(self):
        st.markdown(
            f"""
            <div style="
                background-color: #f0f2f6; 
                padding: 10px 20px; 
                border-radius: 8px; 
                display: flex; 
                justify-content: space-between;
                width: 100%;
                margin: 20px auto;
                color: #333333;
            ">
                <div style="font-weight: bold; font-size: {self.INFO_LABEL_FONT_SIZE};">Estimated Time:</div>
                <div style="font-size: {self.INFO_VALUE_FONT_SIZE}; color: #0072C6;">{self.recipe.estimated_time}</div>
                <div style="font-weight: bold; font-size: {self.INFO_LABEL_FONT_SIZE}; margin-left: 20px;">Difficulty:</div>
                <div style="font-size: {self.INFO_VALUE_FONT_SIZE}; color: #FF5722;">{self.recipe.difficulty}</div>
            </div>
            """, 
            unsafe_allow_html=True
        )

    def display_recipe(self):
        # Set up two columns: left for video, right for text
        col1, col2 = st.columns(2)

        # Display recipe information on the right column
        with col1:
            self.display_title_and_description()
            # Display the estimated time and difficulty
            self.display_time_and_difficulty()
            
            # Display the ingredients for each component
            self.display_ingredients()
            # Display the steps for each component
            if self.step is None:
                self.step = st.empty()
            self.display_current_step()
        with col2:
            st.image("assets/food.jpg", use_column_width=True )
            # Button to start real-time hand estimation
            if st.button("Start Real-Time Hand Estimation"):
                st.session_state.video_running = True
                self.real_time_hand_estimation(col2)  # Pass the left column to the video method


    def real_time_hand_estimation(self, video_column):
        # Use the provided column for video display
        video_container = video_column.empty()  # Container for the video feed in the left column

        # Stop button to control the video feed
        if st.button("Stop Real-Time Hand Estimation"):
            st.session_state.video_running = False

        # Track gesture holding times
        gesture_start_time = None
        current_gesture = None

        # Display the real-time video feed if video_running is True
        while st.session_state.video_running:
            ret, frame = self.cap.read()
            if not ret:
                st.write("Failed to grab frame")
                break

            frame = self.detector.findFingers(frame)
            lmsList, bbox = self.detector.findPosition(frame)

            if len(lmsList) != 0:
                fingers = self.detector.findFingerUp()
                
                # Check if index finger is held up (for next step)
                if fingers[1] == 1 and sum(fingers) == 1:
                    # Start timing if this is a new gesture or continue if same
                    if current_gesture != "next":
                        gesture_start_time = time.time()
                        current_gesture = "next"
                    elif gesture_start_time and time.time() - gesture_start_time >= 0.3:  # Held for 1 second
                        if self.current_step < len(self.recipe.steps) - 1:
                            self.current_step += 1
                            self.display_current_step()
                        gesture_start_time = None  # Reset after action

                # Check if thumb is held up (for previous step)
                elif fingers[0] == 1 and sum(fingers) == 1:
                    # Start timing if this is a new gesture or continue if same
                    if current_gesture != "previous":
                        gesture_start_time = time.time()
                        current_gesture = "previous"
                    elif gesture_start_time and time.time() - gesture_start_time >= 0.3:  # Held for 1 second
                        if self.current_step > 0:
                            self.current_step -= 1
                            self.display_current_step()
                        gesture_start_time = None  # Reset after action
                else:
                    # Reset if no recognized gesture is held
                    gesture_start_time = None
                    current_gesture = None

            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            img = cv.resize(frame, (640, 480))
            video_container.image(img, channels="RGB")  # Update the video feed in the left column

        # Release the camera resource when done
        self.cap.release()