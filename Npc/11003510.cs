using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003510: Gradio
/// </summary>
public class _11003510 : NpcScript {
    internal _11003510(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115009016$ 
                // - Let's get to business. 
                return true;
            case 30:
                // $script:0816160115009017$ 
                // - It's great having friends to hang out with. 
                return true;
            case 40:
                // $script:0816160115009018$ 
                // - I used to work with a friend who loved monsters. I helped my friend's dream come true... 
                return true;
            case 50:
                // $script:0816160115009019$ 
                // - There are no bad monsters. 
                return true;
            case 60:
                // $script:0816160115009020$ 
                // - Why not take a stroll with a little friend? 
                return true;
            default:
                return true;
        }
    }
}
