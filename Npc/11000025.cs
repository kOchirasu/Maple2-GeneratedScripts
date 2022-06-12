using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000025: Beth
/// </summary>
public class _11000025 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;60
    }

    // Select 0:
    // $script:0831180407000138$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000139$
                // - You don't look like you're from around here. Did you come to see the court?
                switch (selection) {
                    // $script:0831180407000140$
                    // - Yep!
                    case 0:
                        return 11;
                    // $script:0831180407000141$
                    // - That's none of your business.
                    case 1:
                        return 13;
                }
                return -1;
            case (11, 0):
                // $script:0831180407000142$
                // - Oh, cool! I was planning on attending myself.
                return 11;
            case (11, 1):
                // $script:0831180407000143$
                // - I asked my brother to see the court with me, but he was more interested in catching some kind of fish while they were in season. I suppose it's good that he didn't come, now that the road to $map:02000001$ is out.
                switch (selection) {
                    // $script:0831180407000144$
                    // - What happened to the road?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0831180407000145$
                // - How could you not have heard? The Royal Road leading to $map:02000001$ was torn up by the earthquake the other day. Can't be good for holding court, y'know?
                return -1;
            case (13, 0):
                // $script:0831180407000146$
                // - Hey, now. No need to be like that. I was just making conversation.
                return -1;
            case (60, 0):
                // $script:1215100607009653$
                // - Fresh fish! We catch 'em, you buy 'em!
                switch (selection) {
                    // $script:1215100607009654$
                    // - I have something to ask you.
                    case 0:
                        return 61;
                }
                return -1;
            case (61, 0):
                // $script:1215100607009655$
                // - Oh, all right. How can I help you, dear?
                switch (selection) {
                    // $script:1215100607009656$
                    // - What can you tell me about trading airships?
                    case 0:
                        return 62;
                }
                return -1;
            case (62, 0):
                // $script:1215100607009657$
                // - You mean those new-fangled boats with wings? They show up in $map:02000062$ from time to time. I've gotta tell you, that's not a sight you'll soon forget.
                switch (selection) {
                    // $script:1215100607009658$
                    // - Have you heard anything about them... disappearing?
                    case 0:
                        return 63;
                }
                return -1;
            case (63, 0):
                // $script:1215100607009659$
                // - Disappearing? Hm... The ones passing through $map:02000062$ never seem to have any trouble...
                switch (selection) {
                    // $script:1215100607009660$
                    // - Have you seen them fly?
                    case 0:
                        return 64;
                }
                return -1;
            case (64, 0):
                // $script:1215100607009661$
                // - Well no, I've never actually seen one in flight. But I can't imagine why they'd have wings if they didn't fly!
                switch (selection) {
                    // $script:1215100607009662$
                    // - Thanks for the information.
                    case 0:
                        return 65;
                }
                return -1;
            case (65, 0):
                // $script:1215100607009663$
                // - Let me know if you ever see one fly.
                switch (selection) {
                    // $script:1215100607009664$
                    // - It seems like the airships traveling by sea are fine...
                    case 0:
                        return 66;
                }
                return -1;
            case (66, 0):
                // $script:1215100607009665$
                // - Uhh. Good? Now are you sure you don't want any fish?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            (13, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.SelectableDistractor,
            (62, 0) => NpcTalkButton.SelectableDistractor,
            (63, 0) => NpcTalkButton.SelectableDistractor,
            (64, 0) => NpcTalkButton.SelectableDistractor,
            (65, 0) => NpcTalkButton.SelectableDistractor,
            (66, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
