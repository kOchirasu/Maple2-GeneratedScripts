using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000527: Hermit
/// </summary>
public class _11000527 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50
    }

    // Select 0:
    // $script:0831180407002251$
    // - Welcome. It's nice to meet you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002254$
                // - $MyPCName$, I can't believe we're meeting again like this. I can see in your eyes how much you've grown since last we met. Do you remember what I told you then? That the world would need a hero? 
                return 30;
            case (30, 1):
                // $script:0831180407002255$
                // - Looking at you now, I believe that you're the one.
                return -1;
            case (40, 0):
                // $script:0831180407002256$
                // - Ha ha ha, you look like you have many questions for me. What do you want to know?
                switch (selection) {
                    // $script:0831180407002257$
                    // - How did you end up on Victoria Island?
                    case 0:
                        return 41;
                    // $script:0831180407002258$
                    // - Why did you save $npcName:11000064[gender:0]$?
                    case 1:
                        return 43;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002259$
                // - This $map:02000051$ is where I was born and raised. The last time I left, I swore I'd never return... I thought that was best for everyone here. 
                return 41;
            case (41, 1):
                // $script:0831180407002260$
                // - But something happened, and it made me wonder if I made the right decision. I came back to finish what I couldn't finish then.
                switch (selection) {
                    // $script:0831180407002261$
                    // - What is it?
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:0831180407002262$
                // - That's... I'll tell you when I'm ready.
                return -1;
            case (43, 0):
                // $script:0831180407002263$
                // - I couldn't ignore the wish of a dying man. Even if he was a prisoner... 
                return 43;
            case (43, 1):
                // $script:0831180407002264$
                // - And when he awoke after his brush with death, I could see in his eyes that he was innocent. I didn't ask any questions, but I knew I had to help him.
                return 43;
            case (43, 2):
                // $script:0831180407002265$
                // - Stay true to yourself, and you can overcome anything. No matter how difficult it is, you can do it.
                return -1;
            case (50, 0):
                // $script:0809153207007164$
                // - Every age needs a hero.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Next,
            (41, 1) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            (43, 0) => NpcTalkButton.Next,
            (43, 1) => NpcTalkButton.Next,
            (43, 2) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
