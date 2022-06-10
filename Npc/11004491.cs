using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004491: Kharadi
/// </summary>
public class _11004491 : NpcScript {
    internal _11004491(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012327$ 
                // - Shh! Quiet! They'll hear us! 
                return true;
            case 10:
                // $script:1227192907012328$ 
                // - Shh! Quiet! They'll hear us! 
                // $script:1227192907012329$ 
                // - I stumbled upon this place quite by accident. I never imagined there might be a large robot factory here. 
                // $script:1227192907012330$ 
                // - See there? The robots are made without any intervention from human factory workers. And with such speed, no less! This explains the endless forces that the Tairen army has managed to field. 
                switch (selection) {
                    // $script:1227192907012331$
                    // - Should I blow this place up, then?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012332$ 
                // - I'm afraid this is but one small corner of the whole facility. What's more, if any part of the factory is destroyed, it's repaired automatically within minutes. 
                // $script:1227192907012333$ 
                // - Any attempt to destroy this place would fail to put any sizable dent in their production capabilities. It would, however, mark our presence on Kritias as a clear threat. A threat that they would feel compelled to wipe out. 
                // $script:1227192907012334$ 
                // - Instead of striking out blindly, we need to understand the full scope of this facility... and what it will take to destroy it once and for all. 
                switch (selection) {
                    // $script:0114164107012723$
                    // - Okay.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0114164107012724$ 
                // - I need to learn more about this facility. 
                return true;
            default:
                return true;
        }
    }
}
