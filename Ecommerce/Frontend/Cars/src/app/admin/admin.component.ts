import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent {



constructor(private router: Router) {}

  navigateToEdit() {
    this.router.navigate(['admin/handleproduct']);
  }

  navigateToOrders() {
    this.router.navigate(['admin/orders']);
  }
navigateToItems() {
    this.router.navigate(['admin/items']);
  }
}
