# Use Case Story Title

<!--- Template Instructions  
  Update the Story Title and remove the warning below.
--->

![warning](./images/misc/warning.png) Before submitting your project repo, modify template as desired and remove all inline  Template Instructions. 

<!--- Template Instructions  
  Organize TOC to meet needs or project
--->
#### Table of Contents
- [Use Case Story Title](#use-case-story-title) 
      - [Table of Contents](#table-of-contents)
  - [Acknowledgements](#acknowledgements)
  - [Business Challenge](#business-challenge)
    - [Concept](#concept)
    - [Approach](#approach)
  - [Vernacular](#vernacular)
  - [Assumptions](#assumptions)
  - [Persona](#persona)
  - [Story](#story)
  - [Demo Workflow](#demo-workflow)
    - [Step 1](#step-1)
    - [Step 2](#step-2)

 
## Acknowledgements

<!--- Template Instructions   
  List any acknowledgements pertaining to the concepts and resources used in this use case story.
--->

1. This scenario leverages a fictitious company called, _Acme Enterprise_. The <img src="./images/persona/acme-logo.png" width="50" height="40"> Acme Enterprise logo is borrowed from [Katie Wickens](https://steins_kake.artstation.com/projects/ebqgb), a graphics designer.
 
## Business Challenge
<!--- Template Instructions   
  Briefly describe the business challenge addressed by this use case story. Design Thinking exercises aid in the development of a clear problem statement. 
--->
 
### Concept
<!--- Template Instructions   
  Briefly describe how this use case applies Atomic Accessibility Design to the business challenge. Leverage Design Thinking exercises to aid in this endeavor. 
--->
 
### Approach
<!--- Template Instructions   
  Describe the end to end interactions of the stakeholders that are pertinent to this use case story. Leverage Design Thinking exercises to aid in this endeavor. 
--->

![pub-workflow](./img/approach.svg)
 
## Vernacular
<!--- Template Instructions   
  List and describe any terms that will be used in the story and referenced in diagrams. The current list provides a sample starter list. Leverage Design Thinking exercises to aid in the identification of use case archetypes. 
--->

## Assumptions
<!--- Template Instructions   
  List any assumptions to be considered in this use case story.  Leverage Design Thinking exercises to aid in this endeavor. 
--->
 
1. *it's assumed that people with disabilities who want to understand a document have access to it in a digital format*

2. *It's assumed that people with disabilities who use the solution have some level of familiarity with digital technology and are able to use a web or messaging application to upload documents*
 
## Persona
<!--- Template Instructions   
  Using the sample persona images in the /images/persona folder, describe the roles of the entities involved in this use case story. The current list provides a sample starter list. 
--->
 
| Actor                                                                    | Role                                   | Goals                                                                                             | Details |
|--------------------------------------------------------------------------|----------------------------------------|---------------------------------------------------------------------------------------------------| --- |
| <img src="./img/Axa.png" width="50" height="50">   Axa                   | Insurance Company                      | Help users with disabilities understand their policies.                                           |  |  
| <img src="./img/Laura.png" width="50" height="40"> Laura                 | Customer Service Representative at Axa | Ensure customers get all the help they need                                                       |  |
| 
| <img src="./img/Peter.png" width="40" height="40"> Mark                  | Person with Disability                 | Has difficulty understanding complex language and would like a solution that helps him understand |  | |
| <img src="./img/ComprehendNow.png" width="40" height="40"> ComprehendNow | Web and Mobile messaging app           | Breakdown complex language in documents so that it's easily understandable.                       | |
 
## Story
<!--- Template Instructions   
  Using the sample persona images in the /images/persona folder, describe the steps that are involved in the interactive use case story. The story below is offered as an exemplar.
--->

<img src="./img/Axa.png" width="50" height="40"> Axa has rolled out new and exciting covers on their insurance policies, they sent out the details of the new covers in a .pdf format to their customers. 

<img src="./img/Peter.png" width="50" height="40"> Mark received the notification from his insurance company AXA informing him that new covers have been added to his policy. He is excited to know more about the new covers, but he is also concerned that he might not be able to understand the information properly due to his cognitive disability.

<img src="./img/Peter.png" width="50" height="40">  Mark decides to contact the insurance company and request for the new policy documents to be explained to him in a simple and clear manner. The customer service representative, <img src="./img/Laura.png" width="50" height="40">  Laura understands <img src="./img/Peter.png" width="50" height="40">  Mark's needs and sends him the link to <img src="./img/ComprehendNow.png" width="50" height="40">  ComprehendNow so that he can find what he needs in the policy document in simplified language and with clear explanations of the new covers.

<img src="./img/Peter.png" width="50" height="40">  Mark is relieved to find that he can easily understand the information and can access it at any time he wants, even from his favorite messaging app. He is also pleased that he can easily ask questions on the policy document if he has any questions or needs clarification.

![process-workflow](./images/workflow/process-workflow.png)

1. <img src="./images/persona/Angelica.png" width="40" height="40"> Angelica opens Theme Building Tool.
2. <img src="./images/persona/Angelica.png" width="40" height="40"> Angelica creates a new design system project within the Theme Building Tool.
3. <img src="./images/persona/Angelica.png" width="40" height="40"> Angelica configures project to produce themes that are either Business (AA) or Government (AAA) [WCAG Compatible][WCAG].
4. <img src="./images/persona/Angelica.png" width="40" height="40"> Angelica adds 10 shades of a color in light and dark mode with corresponding "on color" to the project.
5. <img src="./images/persona/Angelica.png" width="40" height="40"> Angelica defines the base atoms for the theme. This lays the foundation for all light and dark mode calculations. The Theme Building Tool guides <img src="./images/persona/Angelica.png" width="40" height="40"> Angelica through the following steps that **must** occur in sequential order:

   1. Select Primary, Secondary, and Tertiary Colors
   2. Define Light mode background and dark mode background.
   3. Define Gradient backgrounds, Buttons and Icons colors, and Gradient Text.

6. <img src="./images/persona/Angelica.png" width="40" height="40"> Angelica defines other atomic elements (atoms, molecules) that will be used by the theme. The Theme Building Tool guides <img src="./images/persona/Angelica.png" width="40" height="40"> Angelica through the following steps:

   1. Data independent preferences
      1. Specify minimum desktop target area
      2. Specify grid system
      3. Specify animation settings
   2. Data dependent preferences using decisions associated with Primary, Secondary, Tertiary, Light and Dark Mode background colors. These attribute values are calculated:
      1. state colors
      2. Fonts / Typography
      3. Default Border Settings
      4. Elevations
      5. Bevels
      6. Chart colors

7. <img src="./images/persona/Angelica.png" width="40" height="40"> Angelica applies atomic settings to molecules associated with the theme project.
8. <img src="./images/persona/Angelica.png" width="40" height="40"> Angelica uses the Theme Building Tool to generate theme asset types (JSON, CSS, design tokens).
 
## Demo Workflow
<!--- Template Instructions   
  Using the sample persona images in the /images/persona folder, describe the steps of the use case story as they relate to one or more UML Sequence Diagrams.  
--->
 
### Step 1
<img src="./images/persona/Darius.png" width="40" height="40"> Darius conveys impairment preferences to <img src="./images/persona/Angelica.png" width="40" height="40"> Angelica.
 
![step1](./images/uml/sample-sequence-diagram.png)
 
### Step 2
 
<img src="./images/persona/Angelica.png" width="40" height="40"> Angelica uses <img src="./images/persona/themebuilder.svg" width="40" height="40"> Atomic Accessibility Design Tool to generate a theme. 
 
![step2](./images/uml/sample-sequence-diagram.png)