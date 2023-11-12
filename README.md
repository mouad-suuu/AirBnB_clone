# AirBnB Clone Project

## Project Description

Welcome to the AirBnB Clone project, the initial step toward building a comprehensive web application. This phase is crucial as it lays the foundation for subsequent projects, including HTML/CSS templating, database storage, API development, and front-end integration.

### Project Goals

- Implement a parent class, `BaseModel`, responsible for the initialization, serialization, and deserialization of future instances.
- Establish a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> File.
- Create essential classes for AirBnB (User, State, City, Place) that inherit from `BaseModel`.
- Develop the first abstracted storage engine of the project: File storage.
- Implement comprehensive unit tests to validate all classes and the storage engine.

## Description of the Command Interpreter

The command interpreter operates similarly to a shell but is tailored to a specific use-case—managing the objects of the AirBnB project. Key functionalities include:

1. Create a new object (e.g., a new User or Place).
2. Retrieve objects from files, databases, etc.
3. Perform operations on objects (count, compute stats, etc.).
4. Update attributes of an object.
5. Destroy an object.

## How to Start, How to Use, with Examples

### Execution

To run the command interpreter in interactive mode:

```bash
$ ./console.py
