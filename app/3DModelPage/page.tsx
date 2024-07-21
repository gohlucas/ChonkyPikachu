"use client";
import React, { useEffect, useState } from 'react';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import * as THREE from 'three';

const ModelPage: React.FC = () => {
  const [selectedModel, setSelectedModel] = useState('/SoC_COM_1_Basement.glb'); //Default is basement

  useEffect(() => {
    // Scene creation for three.js
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000); //75 Degrees angle
    const renderer = new THREE.WebGLRenderer({ antialias: true });

    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true; 
    controls.dampingFactor = 0.25; 
    controls.screenSpacePanning = false; 
    controls.minDistance = 2; 
    controls.maxDistance = 50; 

    scene.background = new THREE.Color(0xffffff);

    const ambientLight = new THREE.AmbientLight(0xffffff, 1.0);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 1.8);
    directionalLight.position.set(0, 10, 0); //Top down direction
    scene.add(directionalLight);

    const loader = new GLTFLoader(); //GLTF to load 3D model

    let currentModel: THREE.Group | undefined;  //Keep tracks of currently loaded model

    const loadModel = (modelPath: string) => {
      if (currentModel) {
        scene.remove(currentModel); //Remove model if current already have one 
      }
      loader.load(modelPath, (gltf) => {
        currentModel = gltf.scene as THREE.Group;
        scene.add(currentModel);
      });
    };

    loadModel(selectedModel);

    camera.position.set(7.3589, 6.9258, 4.9583); //Initial camera position
    camera.rotation.set(63.55 * (Math.PI / 180), 0, 46.69 * (Math.PI / 180));  //Three.js uses radians

    const animate = () => {
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
    };
    animate();

    //Handles camera aspect ratio when window is resized
    const handleResize = () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    };

    window.addEventListener('resize', handleResize); //Resize when window is changed

    return () => {
      window.removeEventListener('resize', handleResize);
      document.body.removeChild(renderer.domElement);
    };
  }, [selectedModel]);

  //Webpage with selection
  return (
    <div>
      <select onChange={(e) => setSelectedModel(e.target.value)} value={selectedModel}>
        <option value="/SoC_COM_1_Basement.glb">Basement</option>
        <option value="/SoC_COM_1_Level_1.glb">First Floor</option>
        <option value="/SoC_COM_1_Level_2.glb">Second Floor</option>
      </select>
    </div>
  );
};

export default ModelPage;