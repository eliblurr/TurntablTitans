import { Component } from '@angular/core';
import { ThemeServiceService } from 'src/app/theming/theme-service.service';
import { SharedService } from '../services/shared/shared.service';

@Component({
  selector: 'app-accessibility-section',
  templateUrl: './accessibility-section.component.html',
  styleUrls: ['./accessibility-section.component.css']
})
export class AccessibilitySectionComponent {
  constructor(
  private themeService:ThemeServiceService,
  public sharedService: SharedService,
) {}

isDarkMode: Boolean = false;

toggleDarkMode(event: any) {
  this.isDarkMode = event.target.checked;
  if (this.isDarkMode) {
    document.body.classList.add('dark-mode');
    localStorage.setItem('ThemeMode','true');
    this.themeService.changeThemeToDark('B'+localStorage.getItem('BuilderTheme'));
  } else {
    localStorage.setItem('ThemeMode','false');
    document.body.classList.remove('dark-mode');
    this.changeTheme(localStorage.getItem("BuilderTheme"))
  }
}

disabilities: string[] = [
  "Default","Color Blindness", "Dyslexia", "Autism"
];

selectedDisability: any =  localStorage.getItem("BuilderTheme");

ngOnInit(){    
  if(localStorage.getItem("BuilderTheme") === null){
    localStorage.setItem('BuilderTheme','Default');
    this.selectedDisability='Default';
  }
  this.changeTheme(localStorage.getItem("BuilderTheme"))
}

changeTheme(name:any) {
  localStorage.setItem('BuilderTheme',name);
  if (localStorage.getItem('ThemeMode')==='true') {
    this.themeService.changeThemeToDark('B'+localStorage.getItem('BuilderTheme'));
  } 
  else {
    this.themeService.setTheme(name);
  }

}
textToSpeech(text:string){
  this.sharedService.textToSpeech(text, "en")
}


}
