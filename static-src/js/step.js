DOF = function(){
	this.trans = [];
	this.rot = [];
	this.speed = [];
}

step = function(time){
	this.time = time;
	this.DOFs = {};
	this.DOFnum = 0;
}

step.prototype.addDOF = function(name, transX, transY, transZ, rotX, rotY, rotZ, rotW){
	var myDOF = new DOF();
	myDOF.trans[0] = transX;
	myDOF.trans[1] = transY;
	myDOF.trans[2] = transZ;
	myDOF.rot[0] = rotX;
	myDOF.rot[1] = rotY;
	myDOF.rot[2] = rotZ;
	myDOF.rot[3] = rotW;
	this.DOFs[name] = myDOF;
	this.DOFnum++;
}

step.prototype.addSpeed = function(name, speedX, speedY, speedZ){
	this.DOFs[name].speed[0] = speedX;
	this.DOFs[name].speed[1] = speedY;
	this.DOFs[name].speed[2] = speedZ;
}
	
step.prototype.getDOFnum = function(){
	return this.DOFnum;
}

step.prototype.getTransX = function(name){
	return this.DOFs[name].trans[0];
}

step.prototype.getTransY = function(name){
	return this.DOFs[name].trans[1];
}

step.prototype.getTransZ = function(name){
	return this.DOFs[name].trans[2];
}

step.prototype.getSpeedX = function(name){
	return this.DOFs[name].speed[0];
}

step.prototype.getSpeedY = function(name){
	return this.DOFs[name].speed[1];
}

step.prototype.getSpeedZ = function(name){
	return this.DOFs[name].speed[2];
}