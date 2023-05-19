import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {


  username: string = '';

  password: string = '';
  confirmpassword: string = '';


  constructor(private http: HttpClient,private router: Router) { }

  onSubmit() {
    const data = {
      'username': this.username,
      'password': this.password,
      'confirmpassword': this.confirmpassword
    };

    this.http.post('http://127.0.0.1:5000//register', data).subscribe(response => {
      console.log(response);
      // handle success response here
    }, error => {
      console.error(error);
      // handle error response here
    });
    this.router.navigate(['/login']);
  }


}
