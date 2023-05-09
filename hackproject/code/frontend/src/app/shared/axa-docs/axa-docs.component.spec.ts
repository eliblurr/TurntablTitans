import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AXADocsComponent } from './axa-docs.component';

describe('AXADocsComponent', () => {
  let component: AXADocsComponent;
  let fixture: ComponentFixture<AXADocsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AXADocsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AXADocsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
