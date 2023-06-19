import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

interface LoginResponse {
  message: string;
  Assignment: string;
}

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

username: string = '';
password: string = '';


  constructor(private http: HttpClient,private router: Router) { }
  onSubmit() {
    const data = {
      'username': this.username,
      'password': this.password,

    };

   this.http.post<any>('http://127.0.0.1:5000/login', data).subscribe(
  response => {
    console.log(response);

    if (response.message === 'Admin') {
          this.router.navigate(['/admin']); // Redirect admin to the admin page
        }

    else if (response.message === 'Login successful') {

      this.router.navigate(['/home']); // Redirect to the home page
    } else {
      console.log('Invalid credentials'); // Display error message
    }
  },
  error => {
    console.error(error);
    console.log('An error occurred'); // Display error message
  }
);

  }

}
