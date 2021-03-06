import os
import platform

# (1)==================== COMMON CONFIGURATION OPTIONS ======================= #
COMPILER="clang++ -std=c++17"   # The compiler we want to use 
                                #(You may try g++ if you have trouble)
SOURCE="../src/GUI/*.c ../src/JSON/*.c"    # Where the source code lives
# SOURCE_2="../editorSrc/*.cpp"
EXECUTABLE="Enemy_editor"        # Name of the final executable
# EXECUTABLE_2="spriteEditor"
# ======================= COMMON CONFIGURATION OPTIONS ======================= #

# (2)=================== Platform specific configuration ===================== #
# For each platform we need to set the following items
ARGUMENTS=""            # Arguments needed for our program (Add others as you see fit)
INCLUDE_DIR=""          # Which directories do we want to include.
# INCLUDE_DIR_2=""
LIBRARIES=""            # What libraries do we want to include

if platform.system()=="Linux":
    ARGUMENTS="-g -D LINUX" # -D is a #define sent to preprocessor
    INCLUDE_DIR="-I ../include/ ../lib/"
    INCLUDE_DIR_2="-I ../editorInclude/ ../lib/ ../include/SDL2"
    LIBRARIES="-lSDL2 -lSDL2_ttf -lSDL2_mixer -ldl"
elif platform.system()=="Darwin":
    ARGUMENTS="-g -D MAC" # -D is a #define sent to the preprocessor.
    INCLUDE_DIR="-I ../include/ -I/Library/Frameworks/SDL2.framework/Headers"
    INCLUDE_DIR_2="-I../editorInclude/ -I../include/SDL2 -I/Library/Frameworks/SDL2.framework/Headers"
    LIBRARIES="-F/Library/Frameworks -framework SDL2"
elif platform.system()=="Windows":
    COMPILER="gcc -std=c89" # Note we use g++ here as it is more likely what you have
    ARGUMENTS="-g -D MINGW -std=c89 -static-libgcc -static-libstdc++" 
    INCLUDE_DIR="-L../lib -I../include/ -I../include/SDL2 -I../include/GUI -I../include/JSON"
    # INCLUDE_DIR_2="-L../lib -I../editorInclude/ -I../include/SDL2"
    EXECUTABLE="Enemy_editor.exe"
    # EXECUTABLE_2="spriteEditor.exe"
    LIBRARIES="-lmingw32 -lSDL2main -lSDL2 -lSDL2_ttf -lSDL2_image"
# (2)=================== Platform specific configuration ===================== #

# (3)====================== Building the Executable ========================== #
# Build a string of our compile commands that we run in the terminal
compileString=COMPILER+" "+ARGUMENTS+" -o "+EXECUTABLE+" "+" "+INCLUDE_DIR+" "+SOURCE+" "+LIBRARIES
# compileString2=COMPILER+" "+ARGUMENTS+" -o "+EXECUTABLE_2+" "+" "+INCLUDE_DIR_2+" "+SOURCE_2+" "+LIBRARIES
# Print out the compile string
# This is the command you can type
print("============v (Command running on terminal) v===========================")
print("Compilng Debug version(-g) on: "+platform.system())
print(compileString)
# print(compileString2)
print("========================================================================")
# Run our command
os.system(compileString)
# os.system(compileString2)
# ========================= Building the Executable ========================== #


# Why am I not using Make?
# 1.)   I want total control over the system. 
#       Occassionally I want to have some logic
#       in my compilation process (like searching for missing files).
# 2.)   Realistically our projects are 'small' enough 
#       this will not matter.
# 3.)   Feel free to implement your own make files or autogenerate it from this
#       script
# 4.)   It is handy to know Python

