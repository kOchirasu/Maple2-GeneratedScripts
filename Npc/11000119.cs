using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000119: Frey
/// </summary>
public class _11000119 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50;70;120
    }

    // Select 0:
    // $script:0831180407000508$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407000512$
                // - The Royal Guard protects $npcName:11000075[gender:1]$ and all of $map:02000001$. So long as there are threats to peace in this world, we will not rest.
                return -1;
            case (50, 0):
                // $script:0831180407000513$
                // - Maybe it's time I told you the truth about why the court was canceled. Just before it was scheduled to start, the leadership met to discuss the details of the proceedings. Suddenly, a bloodied guard stumbled into the meeting and said that the court must be canceled.
                return 50;
            case (50, 1):
                // $script:0831180407000514$
                // - We were shocked, as you might imagine. And before we could question him further, a dagger flew in from a nearby window and took his life. There, before our very eyes...
                return 50;
            case (50, 2):
                // $script:0831180407000515$
                // - Everyone rushed to find the assailant, but we could find nothing. Our conclusion was that there must be a spy in the palace. The servants of the demon king were plotting something in time for the court. We had to cancel it.
                switch (selection) {
                    // $script:0831180407000516$
                    // - Why didn't you tell anyone what happened?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:0831180407000517$
                // - You expect us to tell the public that someone was murdered, right in the middle of a meeting like that? People have only just started to calm down after the loss of the Blue Lapenta, we don't need to be riling them back up so soon. 
                return -1;
            case (70, 0):
                // $script:1215105107009695$
                // - $MyPCName$, what brings you here?
                switch (selection) {
                    // $script:1215105107009696$
                    // - $npcName:11003534$ sent me.
                    case 0:
                        return 71;
                }
                return -1;
            case (71, 0):
                // $script:1215105107009697$
                // - After all this time as the Guard Captain, $npcName:11003534[gender:0]$ still treats me like a child.
                return 71;
            case (71, 1):
                // $script:1215105107009698$
                // - You go and tell $npcName:11003534$ that I'll do whatever's necessary to protect $npc:11000075[gender:1]$ and $npcName:11000601[gender:1]$. I swore an oath, and on my life I intend to keep it.
                switch (selection) {
                    // $script:1215105107009699$
                    // - Uh, I'm actually here to ask about the rumors going around $map:02000001$.
                    case 0:
                        return 72;
                }
                return -1;
            case (72, 0):
                // $script:1215105107009700$
                // - Ugh, not you too. These rumors are giving me a headache. I've upped security and tripled patrols to reassure the public, yet the rumors continue to spread.
                switch (selection) {
                    // $script:1215105107009701$
                    // - And what about the truth behind the rumors?
                    case 0:
                        return 73;
                }
                return -1;
            case (73, 0):
                // $script:1215105107009702$
                // - I'll tell you the same thing I told the former captain of the Knights when he stopped by. I don't know anything! If we had any insight into the circumstances behind the rumors, the alliance would be the first to know.
                switch (selection) {
                    // $script:1215105107009703$
                    // - The former captain?
                    case 0:
                        return 74;
                }
                return -1;
            case (74, 0):
                // $script:1215105107009704$
                // - Ah, it's nothing. Don't worry about it.
                switch (selection) {
                    // $script:1215105107009705$
                    // - Okay.
                    case 0:
                        return 75;
                }
                return -1;
            case (75, 0):
                // $script:1215105107009706$
                // - I'm sorry I couldn't be of more help.
                return -1;
            case (120, 0):
                // $script:0831180407000518$
                // - Some people are curious about my relationship with $npcName:11000076[gender:0]$. It's... quite complicated. I'd rather not get into it.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Next,
            (50, 2) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Close,
            (70, 0) => NpcTalkButton.SelectableDistractor,
            (71, 0) => NpcTalkButton.Next,
            (71, 1) => NpcTalkButton.SelectableDistractor,
            (72, 0) => NpcTalkButton.SelectableDistractor,
            (73, 0) => NpcTalkButton.SelectableDistractor,
            (74, 0) => NpcTalkButton.SelectableDistractor,
            (75, 0) => NpcTalkButton.Close,
            (120, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
