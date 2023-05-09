import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AXAInputComponent } from './axa-input.component';

describe('AXADocsComponent', () => {
  let component: AXAInputComponent;
  let fixture: ComponentFixture<AXAInputComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AXAInputComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AXAInputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
