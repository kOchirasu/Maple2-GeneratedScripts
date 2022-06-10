using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000839: Pochi
/// </summary>
public class _11000839 : NpcScript {
    internal _11000839(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003069$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:0831180407003072$ 
                // - Do you know who $npcName:11000614[gender:0]$ is? He's a friend of mine in $map:03000135$.
                // $script:0831180407003073$ 
                // - We first met in Katramus. The Lumina Liberation Army sprung us while we were being transferred to another prison, and we joined up together. 
                // $script:0831180407003074$ 
                // - We promised that we'd stick together like we did during our time in prison. That was the most difficult time of our lives.
                return true;
            default:
                return true;
        }
    }
}
