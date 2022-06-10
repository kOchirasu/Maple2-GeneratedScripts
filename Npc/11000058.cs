using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000058: Elmin
/// </summary>
public class _11000058 : NpcScript {
    internal _11000058(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000255$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407000258$ 
                // - If I had stayed with Bella that day...  
                return true;
            case 40:
                // $script:0831180407000259$ 
                // - I used to live here with my family, but... I'm the only one living in this house now. I miss them so much... 
                return true;
            case 50:
                // $script:0831180407000260$ 
                // - Sometimes I sit by the window, watching the stars fade away one by one, reminiscing about the good old days. I try not to recall the sad memories, but only the good, happy ones. 
                return true;
            default:
                return true;
        }
    }
}
