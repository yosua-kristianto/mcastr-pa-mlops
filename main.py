"""model_builder
This module is responsible for orchestrating building emo analysis model for this project.
This main file, serves as the entry point and orchestrates all required components 
in the model building process.

1. Update Knowledge Base database
2. Fetch data from the database
3. Convert the fetched data into Pandas DataFrame

// These processes below are forked from https://github.com/yosua-kristianto/McAstr/tree/development/McAstr%20ML
4. Data Normalization (Data Pre-Processing)
5. Model Training
6. Model Evaluation
7. Model Saving

"""
import argparse

def main():
    ""
    

if __name__ == "__main__":
    from datetime import datetime

    print(f"""
    __       __             ______               __                      __       __  __         ______                      
/  \     /  |           /      \             /  |                    /  \     /  |/  |       /      \                     
$$  \   /$$ |  _______ /$$$$$$  |  _______  _$$ |_     ______        $$  \   /$$ |$$ |      /$$$$$$  |  ______    _______ 
$$$  \ /$$$ | /       |$$ |__$$ | /       |/ $$   |   /      \       $$$  \ /$$$ |$$ |      $$ |  $$ | /      \  /       |
$$$$  /$$$$ |/$$$$$$$/ $$    $$ |/$$$$$$$/ $$$$$$/   /$$$$$$  |      $$$$  /$$$$ |$$ |      $$ |  $$ |/$$$$$$  |/$$$$$$$/ 
$$ $$ $$/$$ |$$ |      $$$$$$$$ |$$      \   $$ | __ $$ |  $$/       $$ $$ $$/$$ |$$ |      $$ |  $$ |$$ |  $$ |$$      \ 
$$ |$$$/ $$ |$$ \_____ $$ |  $$ | $$$$$$  |  $$ |/  |$$ |            $$ |$$$/ $$ |$$ |_____ $$ \__$$ |$$ |__$$ | $$$$$$  |
$$ | $/  $$ |$$       |$$ |  $$ |/     $$/   $$  $$/ $$ |            $$ | $/  $$ |$$       |$$    $$/ $$    $$/ /     $$/ 
$$/      $$/  $$$$$$$/ $$/   $$/ $$$$$$$/     $$$$/  $$/             $$/      $$/ $$$$$$$$/  $$$$$$/  $$$$$$$/  $$$$$$$/  
                                                                                                      $$ |                
                                                                                                      $$ |                
                                                                                                      $$/                 
    
    Session {datetime.now()}
    """)


    main()