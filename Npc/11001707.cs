using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001707: Tinchai
/// </summary>
public class _11001707 : NpcScript {
    internal _11001707(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006959$ 
                // - Mm? Yes?
                return true;
            case 30:
                // $script:0728024507006983$ 
                // - Hello again. Is there something you need?
                switch (selection) {
                    // $script:0804030507007012$
                    // - How is $npcName:11001715[gender:0]$?
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0804030507007013$
                    // - What do you think of $map:02000001$?
                    case 1:
                        Id = 50;
                        return false;
                }
                return true;
            case 40:
                // $script:0804030507007014$ 
                // - You aren't actually <i>worried</i> about him, are you? He'll be soooo happy to hear that!
                switch (selection) {
                    // $script:0804030507007015$
                    // - I'm not worried! Just... concerned.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0804030507007016$ 
                // - Well, he'll appreciate your concern, anyway. I'm keeping a close eye on him, so you just leave him to me.
                // $script:0804030507007017$ 
                // - <font color="#909090">($npcName:11001707[gender:1]$ stops talking suddenly. She hesitates for a moment, then speaks.)</font>
                //   $MyPCName$... Thank you.
                switch (selection) {
                    // $script:0804030507007018$
                    // - What for?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:0804030507007019$ 
                // - $npcName:11001715[gender:0]$ has always been very hard on you. But you've stood by us through this crisis, when other students abandoned us for far less.
                // $script:0804030507007020$ 
                // - Now Halo Mountain has been burned to the ground and the master is gone. Guidance exists in name only. You have no real obligation to us. Why don't you wash your hands of this whole mess?
                switch (selection) {
                    // $script:0804030507007021$
                    // - I owe the master my life.
                    case 0:
                        Id = 43;
                        return false;
                }
                return true;
            case 43:
                // $script:0804030507007022$ 
                // - Maybe... But I want to thank you anyway. That's all.
                switch (selection) {
                    // $script:0804030507007023$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 50:
                // $script:0804030507007024$ 
                // - This place is amazing! I've never seen such a big city before. It's loud and crowded and crazy, but I think I see why humans like it here.
                // $script:0804030507007025$ 
                // - I also get why students who completed their training came to live here. It's about as different from life on Halo Mountain as you can get.
                switch (selection) {
                    // $script:0804030507007026$
                    // - So, you think you'll be a city slicker from now on?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:0804030507007027$ 
                // - No, I don't think so. This place is amazing, but I'll always choose a peaceful life on Halo Mountain...
                //   <font color="#909090">(There's a far-off look in her eyes.)</font>
                // $script:0804030507007028$ 
                // - N-no need to dwell on the past, I guess! Let's talk about something else.
                return true;
            default:
                return true;
        }
    }
}
