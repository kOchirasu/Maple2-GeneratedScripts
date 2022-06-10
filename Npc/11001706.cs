using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001706: Tinchai
/// </summary>
public class _11001706 : NpcScript {
    internal _11001706(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006958$ 
                // - Mm? Yes?
                return true;
            case 30:
                // $script:0728024507006980$ 
                // - It's good to see you, $MyPCName$. Is there something I can get for you?
                switch (selection) {
                    // $script:0804030507007003$
                    // - What is this artifact we're after?
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0804030507007004$
                    // - Should we be looking for the master?
                    case 1:
                        Id = 50;
                        return false;
                }
                return true;
            case 40:
                // $script:0804030507007005$ 
                // - I don't know exactly what it is, but supposedly Lone Spirit, the founder of Guidance, left behind a treasure that would grant enlightenment to his true heir. It was passed down through generations... until the eleventh Munakra vanished with it.
                // $script:0804030507007006$ 
                // - Some people think it was destroyed. Others think that all of its power was drained, and it's been placed in hiding until it can recharge. Others say that Lone Spirit reincarnated and claimed it for himself. Who knows which theory, if any, is true?
                // $script:0804030507007007$ 
                // - The only reliable information on the artifact is told through word-of-mouth, so the only one who would really know is the master. What if... what if $npcName:11001559[gender:0]$ came to Halo Mountain for the artifact?
                // $script:0804030507007008$ 
                // - That must be it. I'm sure he said something about an artifact when he attacked us...
                //   <font color="#909090">($npcName:11001706[gender:1]$ is lost in thought.)</font>
                switch (selection) {
                    // $script:0804030507007009$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 50:
                // $script:0804030507007010$ 
                // - The master can fend for himself. Don't worry, all right?
                //   <font color="#909090">(Even as she comforts you, worry is etched in her face.)</font>
                switch (selection) {
                    // $script:0804030507007011$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
