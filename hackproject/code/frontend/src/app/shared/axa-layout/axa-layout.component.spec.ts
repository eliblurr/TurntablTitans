import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AxaLayoutComponent } from './axa-layout.component';

describe('AxaLayoutComponent', () => {
  let component: AxaLayoutComponent;
  let fixture: ComponentFixture<AxaLayoutComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AxaLayoutComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AxaLayoutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
