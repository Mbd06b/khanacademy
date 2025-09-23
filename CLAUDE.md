# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a legacy Khan Academy codebase, representing an early version of the educational platform. It's a Python-based Google App Engine application that provides math exercises, video content, and student progress tracking.

## Architecture

### Core Application Structure
- **Python/Django on Google App Engine**: Legacy GAE Python runtime with Django templates
- **Main entry point**: `main.py` contains URL routing and request handlers
- **Base handler**: `request_handler.RequestHandler` extends GAE's `webapp.RequestHandler` with utility methods
- **Models**: `models.py` contains Google App Engine datastore models (UserData, Exercise, Video, etc.)

### Key Components
- **Exercises**: Math problem generators with JavaScript-based UI
- **Videos**: Educational video content with progress tracking
- **User Management**: Student accounts, progress tracking, and coach relationships
- **Knowledge Map**: Topic organization and prerequisite tracking
- **Discussion System**: Q&A and comments on exercises/videos
- **Badges**: Achievement system for student motivation
- **API**: RESTful endpoints for data access

### Data Models
- `UserData`: Student accounts and progress
- `Exercise`: Math exercise definitions
- `Video`: Educational video metadata
- `UserExercise`: Student progress on specific exercises
- `ProblemLog`: Individual problem attempt history
- `VideoLog`: Video viewing history

## Development Commands

This is a Google App Engine application with no standard build system. Development is done directly with GAE dev server.

### Running the Application
```bash
# Start GAE development server (typical command for legacy GAE)
dev_appserver.py .
```

### Configuration Files
- `app.yaml`: GAE application configuration
- `index.yaml`: Datastore index definitions
- `cron.yaml`: Scheduled task definitions
- `mapreduce.yaml`: MapReduce job configurations

## File Organization

- **HTML Templates**: Exercise templates (e.g., `addition_1.html`, `algebra_*.html`)
- **Static Assets**:
  - `/images/`: Icons and graphics
  - `/javascript/`: Client-side exercise logic
  - `/stylesheets/`: CSS styling
- **Python Modules**:
  - `models.py`: Data model definitions
  - `util.py`: Common utilities
  - `points.py`: Points/scoring system
  - `coaches.py`: Teacher/student relationships
  - `api.py`: API endpoints

## Exercise System

Exercises are HTML templates with embedded JavaScript that generate math problems dynamically. Each exercise file represents a specific math topic with interactive problem generation.

## Important Notes

- This is a legacy codebase using deprecated GAE Python runtime
- No modern build tools (no npm, pip requirements, etc.)
- Uses Django templates but not full Django framework
- Static file serving configured in `app.yaml`
- Admin functions require Google account login