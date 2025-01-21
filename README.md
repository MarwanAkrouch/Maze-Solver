Our software is designed to solve a problem of route optimization by passing through target
points with the presence of obstacles, we took the case of a client who wants to get all the
products on his list and leave in a optimal route.
The supermarket offers its client the possibility to choose the products he needs through a
web interface and an optimal path will be calculated for him. This problem is a variant of the
travelling salesman problem, we solved it in two different ways, we used operational research
tools through Google OR libraries in python for the first solver, and Q-learning algorithm for
the second. Since our algorithms are implemented in python we used django framework to build
the web interface for the user.


1. **Install the requirements**:
   ```sh
   pip install -r requirements.txt
    ```

2. **Apply the migrations**:
   ```sh
   python src/supermarket/manage.py migrate
    ```

3. **Run the Django development server**:
   ```sh
   python src/supermarket/manage.py runserver
    ```

Choose products you want to add to your list, then choose the solver to use for getting the optimal path, and voilà !
