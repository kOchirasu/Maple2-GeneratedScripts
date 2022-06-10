using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000987: Horok
/// </summary>
public class _11000987 : NpcScript {
    internal _11000987(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003401$ 
                // - Hey, how did you find this place? 
                return true;
            case 20:
                // $script:0831180407003403$ 
                // - It's coming, and we don't have much time left. We must find shelter quickly.  
                return true;
            default:
                return true;
        }
    }
}
