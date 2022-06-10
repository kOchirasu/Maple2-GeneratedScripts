using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001699: Tinchai
/// </summary>
public class _11001699 : NpcScript {
    internal _11001699(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0711210007006724$ 
                // - Mm? Yes? 
                return true;
            case 30:
                // $script:0727223007006903$ 
                // - How can I help you? 
                switch (selection) {
                    // $script:0727223007006904$
                    // - $npcName:11001557[gender:0]$ is a tough teacher.
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0727223007006905$ 
                // - You don't need to tell <i>me</i> that. He's the reason some of our old students left! 
                // $script:0727223007006906$ 
                // - $npcName:11001557[gender:0]$ cares about only one thing, and that's training. He expects everyone to keep up with him, and the problem with that should be obvious. 
                // $script:0727223007006907$ 
                // - I will say, he has a talent for crushing confidence, and that's important when you get arrogant students. His heart's in the right place, it's just... cold and unfeeling, you know? 
                // $script:0727223007006908$ 
                // - If you ask him why all those students left, he'd tell you they were too soft. Even if he's right, he's not helping them by driving them away! 
                return true;
            default:
                return true;
        }
    }
}
