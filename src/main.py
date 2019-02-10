from src.SceneFileReader import SceneFileReader
from src.SceneManager import SceneManager
from src.DataBaseManager import DataBaseManager as db_manager
import traceback

#FILENAME = "../../sample_stories/street_story_json.json"
FILENAME = "../sample_stories/simplified_street.json"


if __name__=="__main__":

 try:
    #Connect to the database
    db_manager("mongodb://localhost:27017/").connect()
    #Read the output of the NLP module
    scene_file_reader = SceneFileReader(FILENAME) # May be change that to a string
    scene_nodes = scene_file_reader.readFile()
    #Create the scene manager
    app = SceneManager(scene_nodes)
    #run the application
    app.run()
 except Exception:
     traceback.print_exc()
     print("The application has stopped working")



