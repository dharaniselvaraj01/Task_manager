# Use the official miniconda3 base image
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the environment.yml file
COPY environment.yml .

# Create the environment from the environment.yml
RUN conda env create -f environment.yml

# Activate the environment and install Django and other dependencies
RUN echo "source activate <your-env-name>" > ~/.bashrc
ENV PATH /opt/conda/envs/<your-env-name>/bin:$PATH

# Copy your Django project code
COPY . .

# Expose the port your app runs on
EXPOSE 8000

# Run the Django application
CMD ["bash", "-c", "source activate <your-env-name> && python manage.py runserver 0.0.0.0:8000"]
