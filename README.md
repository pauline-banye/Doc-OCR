# Document Understanding and Optical Character Recognition (OCR) Project

> ## Table of contents

- [Overview](#overview)
- [Objectives](#objectives)
- [Project Scope](#project-scope)
- [Technologies](#technologies)
- [Repo Setup](#repo-setup)
- [Setting up the project](#setting-up-the-project)
  - [Download and install software](#1-download-and-install-software)
  - [Create virtual environment](#2-create-virtual-environment)
- [Status of the project](#status)
- [License information](#license)


> ## Overview

In recent years, technology for Document Understanding and Optical Character Recognition (OCR) has made huge strides. It offers powerful solutions to extract text and structured data from images and scanned documents. 

<p align="center" width="100%">
  <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.edenai.co%2Fpost%2Fanalyze-easily-document-files-with-ai-optical-character-recognition-ocr&psig=AOvVaw36cJPVuZTKNJpe8ZtenAtW&ust=1706451183161000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCOjMraDg_YMDFQAAAAAdAAAAABAg" alt="site"/>
</p>


- **Efficiency Boost**: Implementing Document Understanding and OCR will streamline document processing, cutting down the time needed for data extraction.
- **Improved Data Access**: Digitizing physical documents will centralize data storage, making it easier to find and retrieve information swiftly.
- **Cost Savings**: By reducing manual data entry, we can save costs and allocate resources to more valuable tasks.
- **Better Customer Experience**: Quicker document processing means faster responses, leading to a more satisfying experience for our customers.

#

> ## Objectives:

- Develop an automated Document Understanding system capable of extracting text and structured data from various document types, including handwritten forms and printed contracts.
- Maintain a minimum accuracy rate of 95% in data extraction to minimize errors.
- Centralize document storage and establish a secure and easily accessible digital repository.
- Reduce document processing time by 50% within the first six months of implementation.
- Ensure compliance with industry regulations and standards in data handling and storage.

#

> ## Project Scope:

- **Data Collection**: We'll gather documents to understand how to build the OCR extractor.
- **Web Interface**: We'll create a simple web interface for the solution.
- **Designing the Architecture**: We'll get a rough idea of how the solution should be built.
- **Text Extraction Pipeline**: We'll build a basic text extractor from PDFs into the solution.
- **Deployment**: We'll deploy the solution to run locally or on a Cloud service.
- **Table Extraction Pipeline**: We'll develop a basic table extractor from PDFs into the solution.

#
> ## Technologies

<p align="justify">
This project was setup and developed on a system running Windows 10. The tech tools used for this project include:
</p>

| <b><u>Stack</u></b>          | <b><u>Usage</u></b>   |
| :--------------------------- | :-------------------- |
| **`Python 3.10.13`**             | Programming language. |                 |
| **`Anaconda`** | Package management                 |
| **`Visual Studio Code`** | Code editor |

#

> ## Setting up the project

<p align="justify">
Clone the the Doc-OCR repository to create a copy on your local machine.
</p>

    $ https://github.com/pauline-banye/Doc-OCR.git



### 1.  Download and install software
The first step requires the download and installation of [Python](https://www.python.org/downloads/), [Visual Studio Code](https://code.visualstudio.com/download) and [Anaconda](https://www.anaconda.com/download#downloads). After the installation of the Python program, setup the project with an anaconda environment in the command prompt, powershell or gitbash terminal. This helps to create an isolated Python environment containing all the packages necessary for the project.

- \*Note: This project was setup using the gitbash terminal. Some of the commands used may not work with command prompt or powershell. 

### 2.  Create virtual environment
Navigate to the cloned local project folder. Create a virtual environment folder and activate the environment by running the following commands in the gitbash terminal.

###

    $ conda create <name of virtual environment>
    $ conda activate <name of virtual environment>

<p align="justify">
Once the virtual environment is active, the next step is the installation of the dependencies for the project. A few of them are listed below.

| <b><u>Modules</u></b>     | <b><u>Usage</u></b>           |
| :------------------------ | :---------------------------- |
| **`numpy`**            | Scientific computing              |
| **`pytesseract `**          | OCR tool                  |
| **`Sentence transformers 2.2.2`**                | Multilingual Sentence Embeddings     |
| **`Llama-cpp-python 0.23.33`** | Large language model

<p align="justify">
An exhaustive list can be found in the environment.yml file included in this project. The modules can be 'batch installed' using the `conda env update --file environment.yml` command.

**Alternative method**
You can create the conda enviromnent from the environment.yml file.

    $ conda env update -n <name of virtual environment> -f environment.yml


> ## Running the project
>
Type this command to run the project

    $ streamlit run main.py


#
> ## Status
>
This project is a work in progress and is currently under development.

#

> ## License

This project is licensed under the [MIT License](LICENSE). Feel free to contribute and use it as you see fit.

#
###### Readme created by Pauline Banye