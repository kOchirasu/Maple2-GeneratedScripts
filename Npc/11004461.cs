using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004461: Safehold Guardsman
/// </summary>
public class _11004461 : NpcScript {
    internal _11004461(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012070$ 
                // - All's well!
                return true;
            case 10:
                // $script:1227192907012071$ 
                // - All's well!
                // $script:1227192907012072$ 
                // - Two months out from retirement, and I get assigned here. Just my luck.
                // $script:1227192907012073$ 
                // - Forget justice and duty! I want to go home!
                switch (selection) {
                    // $script:1227192907012074$
                    // - Stick with it, soldier!
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012075$ 
                // - No way. I don't have what it takes to be a hero! I just want to go hide under my bunk!
                // $script:1227192907012076$ 
                // - Don't tell Condor about this, by the way. If he hears I've been talking like this, I'm done for!
                return true;
            default:
                return true;
        }
    }
}
