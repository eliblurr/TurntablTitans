import { Component, OnInit } from '@angular/core';
import { AudioRecorderService } from '../services/recorder/recorder.service'
import {SynthesisService} from "../services/text-speech-synth/synthesis.service"
import { DomSanitizer } from "@angular/platform-browser";
import { SharedService } from '../services/shared/shared.service';

@Component({
  selector: 'recorder',
  templateUrl: './recorder.component.html',
  styleUrls: ['./recorder.component.css']
})
export class RecorderComponent implements OnInit{
  isRecording = false;
  recordedTime: any;
  blobUrl: any;
  blob: any;
  teste:any;

  constructor(
    private audioRecordingService:AudioRecorderService,
    private synthesisService:SynthesisService,
    public sharedService: SharedService,
    private sanitizer: DomSanitizer
  ) {
    this.audioRecordingService
      .recordingFailed()
      .subscribe(() => (this.isRecording = false));
    this.audioRecordingService
      .getRecordedTime()
      .subscribe(time => (this.recordedTime = time));
    this.audioRecordingService.getRecordedBlob().subscribe(data => {
      this.teste = data;
      this.blob = data.blob;
      this.blobUrl = this.sanitizer.bypassSecurityTrustUrl(
        URL.createObjectURL(data.blob)
      );
    });
  }

  ngOnInit(){    
    if(localStorage.getItem("BuilderTheme") === null){
      localStorage.setItem('BuilderTheme','Default');
    }
  }

  startRecording() {
    if (!this.isRecording) {
      this.isRecording = true;
      this.audioRecordingService.startRecording();
    }
  }

  abortRecording() {
    if (this.isRecording) {
      this.isRecording = false;
      this.audioRecordingService.abortRecording();
    }
  }

  stopRecording() {
    if (this.isRecording) {
      this.audioRecordingService.stopRecording();
      this.isRecording = false;
    }
  }

  clearRecordedData() {
    this.blobUrl = null;
    this.recordedTime=null;
  }

  ngOnDestroy(): void {
    this.abortRecording();
  }

  submitAudio(){
    const chatId = this.sharedService.chatId;
    console.log(this.blob)
    console.log(this.teste)
    this.synthesisService.fetch_text(this.blob, "audio.wav", chatId).subscribe(
      (res:string)=>{
        console.log(res)
      }
    )
  }


}
