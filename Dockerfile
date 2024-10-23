# Use the official miniconda3 base image
FROM continuumio/miniconda3


# Copy the environment.yml file
COPY environment.yml .

# Create the environment from the environment.yml
RUN conda env create -f environment.yml

# Activate the environment and install Django and other dependencies
RUN echo "source activate taskmanager" > ~/.bashrc
ENV PATH /opt/conda/envs/taskmanager/bin:$PATH

# Copy your Django project code
COPY . .

# Set the working directory
WORKDIR taskmanager/tasks



# Expose the port your app runs on
EXPOSE 8000

# Run the Django application
CMD ["bash", "-c", "source activate taskmanager> && python manage.py runserver 0.0.0.0:8000"]
