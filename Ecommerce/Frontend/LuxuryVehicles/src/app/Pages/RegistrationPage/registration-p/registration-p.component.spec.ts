import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistrationPComponent } from './registration-p.component';

describe('RegistrationPComponent', () => {
  let component: RegistrationPComponent;
  let fixture: ComponentFixture<RegistrationPComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegistrationPComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RegistrationPComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
