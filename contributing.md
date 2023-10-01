# Contributing to CONTRIBUTING.md

First off, thanks for taking the time to contribute! 

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues


## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Your First Code Contribution](#your-first-code-contribution)
- [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
- [Commit Messages](#commit-messages)
- [Join The Project Team](#join-the-project-team)


## Code of Conduct

This project and everyone participating in it is governed by the
[CONTRIBUTING.md Code of Conduct](blob/master/CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable behavior
to <>.


## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation]().

Before you ask a question, it is best to search for existing [Issues](/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (nodejs, npm, etc), depending on what seems relevant.

We will then take care of the issue as soon as possible.



## I Want To Contribute

> ### Legal Notice 
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.

### Reporting Bugs


#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](issues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
- Stack trace (Traceback)
- OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
- Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
- Possibly your input and the output
- Can you reliably reproduce the issue? And can you also reproduce it with older versions?


#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to <>.


We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).




### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for CONTRIBUTING.md, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.


#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation]() carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.


#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux. 
- **Explain why this enhancement would be useful** to most CONTRIBUTING.md users. You may also want to point out the other projects that solved it better and which could serve as inspiration.



### Your First Code Contribution

Welcome to the community! Before making your first code contribution, please ensure you have set up the project locally and have familiarized yourself with the codebase. Here's how you can make your first contribution:

1.Fork the Repository: Start by forking the main repository to your GitHub account. This will create a copy of the project under your account.

2.Clone the Repository: Clone the forked repository to your local machine using the following command:

**git clone https://github.com/codewithnick/searchenginepy.git**

3.Create a New Branch: Create a new branch for your contribution. Use a descriptive branch name that reflects the nature of your changes:
**git checkout -b feature/your-feature-name**

4.Make Changes: Write your code, add new features, or fix bugs. Ensure your code follows the project's coding style and conventions.

5.Test Your Changes: Before submitting your contribution, make sure to test your changes thoroughly. Run the existing tests and add new ones if necessary to validate your modifications.

6.Commit Your Changes: Commit your changes with a clear and concise commit message that explains the purpose of your changes:
**git commit -m "Add description of your changes"**

7.Push Your Changes: Push your changes to your forked repository on GitHub:
**git push origin feature/your-feature-name**

8.Create a Pull Request: Go to the original repository on GitHub and create a new pull request. Provide a detailed description of your changes in the pull request template. Your pull request will be reviewed, and feedback may be provided.


### Improving The Documentation
Clear and comprehensive documentation is crucial for the project's users and contributors. If you want to improve the documentation:

**Identify Documentation Gaps**: Review the existing documentation to identify areas that can be improved or expanded. This could include installation guides, usage examples, or API documentation.

**Write Clear and Concise Content**: When adding or modifying documentation, ensure that the language is clear, concise, and easy to understand. Use examples and code snippets where applicable to illustrate usage.

**Update README and Usage Guides**: If you're adding new features, make sure to update the project's README file and any usage guides to reflect these changes. Users should have a clear understanding of how to use the new features.

**Correct Errors and Typos**: If you find any errors or typos in the existing documentation, feel free to fix them. Attention to detail is key to maintaining high-quality documentation.

## Styleguides
### Commit Messages
When making commits to the project, follow these guidelines for clear and informative commit messages:

1.Use present tense and imperative mood (e.g., "Add feature" instead of "Added feature").

2.Keep the subject line concise and descriptive, summarizing the purpose of the commit in 50 characters or less.

3.If needed, provide a detailed description of the changes in the commit body. Mention why the change was made and how it affects the project.


## Join The Project Team

Contributors who consistently demonstrate their expertise, dedication, and understanding of the project may be invited to join the project team. Project team members have direct access to merge changes into the main repository.

If you are interested in becoming a project team member, actively participate in discussions, provide valuable contributions, and help other community members. Your contributions will be recognized and considered for team membership.

Thank you for your interest in contributing to **SearchEnginePy**! Your contributions are highly valued, and together, we can create a powerful and efficient search engine for the command line. Happy coding! 🚀
