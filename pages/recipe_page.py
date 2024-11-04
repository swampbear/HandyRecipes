import streamlit as st
from hand_estimation import HandEstimation
import cv2 as cv
from models.Recipe import Recipe

class RecipePage:
    def __init__(self, recipe: Recipe):
        self.detector = HandEstimation()
        self.cap = cv.VideoCapture(0)
        self.recipe = recipe
        self.scroll = st.empty()
        
        # Initialize session state for managing video feed
        if "video_running" not in st.session_state:
            st.session_state.video_running = False
        if "recipe_page" not in st.session_state:
            st.session_state.recipe_page = None
    
    def display_ingrediants(self):
        st.write("Ingredients:")
        for component in self.recipe.recipe_components:
            st.write(f"{component.name}")
            for ingredient in component.ingredients_per_portion:
                st.write(f"  - {ingredient}")
    
    def display_steps(self):
        st.write("Steps:")
        for step in self.recipe.steps:
            st.write(f"{step.number}. {step.description}")

    def display_recipe(self):
        # Set up two columns: left for video, right for text
        col1, col2 = st.columns(2)

        # Display recipe information on the right column
        with col1:
            st.title(self.recipe.title)
             # Button to start real-time hand estimation
            if st.button("Start Real-Time Hand Estimation"):
                st.session_state.video_running = True
                self.real_time_hand_estimation(col2)  # Pass the left column to the video method

            st.write(self.recipe.description)
            st.write("Ingredients:")
            st.write(f" Estimated time: {self.recipe.estimated_time}")
            st.write(f"Difficulty: {self.recipe.difficulty}")
            # Display the ingredients for each component
            self.display_ingrediants()
            # Display the steps for each component
            self.display_steps()

            
           
    def real_time_hand_estimation(self, video_column):
        # Use the provided column for video display
        video_container = video_column.empty() # Container for the video feed in the left column

        # Stop button to control the video feed
        if st.button("Stop Real-Time Hand Estimation"):
            st.session_state.video_running = False

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
                # Scroll down if index finger is up
                if fingers[1] == 1 and sum(fingers) == 1:
                    self.scroll.write("Scroll Down")
                # Scroll up if thumb is up
                elif fingers[0] == 1 and sum(fingers) == 1:
                    self.scroll.write("Scroll Up")
                    
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            img = cv.resize(frame, (640, 480))
            video_container.image(img, channels="RGB")  # Update the video feed in the left column

        # Release the camera resource when done
        self.cap.release()

# Example usage
if __name__ == "__main__":
    sample_recipe = Recipe(title="Handy Recipe for Hand Detection", description="This recipe demonstrates real-time hand detection.")
    st.session_state.recipe_page = RecipePage(sample_recipe)
    st.session_state.recipe_page.display_recipe()