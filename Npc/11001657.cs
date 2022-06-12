using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001657: Junta
/// </summary>
public class _11001657 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0617105607006367$
    // - More questions?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0727223007006865$
                // - Halo Mountain...
                switch (selection) {
                    // $script:0727223007006866$
                    // - Is the master really gone?
                    case 0:
                        return 40;
                    // $script:0727223007006867$
                    // - What do we do now?
                    case 1:
                        return 50;
                    // $script:0727223007006868$
                    // - Who was that?
                    case 2:
                        return 60;
                }
                return -1;
            case (40, 0):
                // $script:0727223007006869$
                // - I doubt we've seen the last of him. His command of animus is unlike anything I've ever seen. And until he returns, I will do everything I can to protect Guidance.
                switch (selection) {
                    // $script:0727233607006921$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (50, 0):
                // $script:0727223007006870$
                // - I know that we need to evaluate our options carefully... But all I want to do right now is destroy something. I will be deferring to $npcName:11001656[gender:1]$ for now.
                switch (selection) {
                    // $script:0727233607006922$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (60, 0):
                // $script:0727223007006871$
                // - I've never seen or heard of him before. Strange that the master never mentioned him, but it sounds like this Kandura lost the title of Munakra to him and has held a grudge ever since.
                return 60;
            case (60, 1):
                // $script:0727223007006872$
                // - The power he wields wasn't pure animus. The darkness tainting it was potent.
                switch (selection) {
                    // $script:0727223007006873$
                    // - If I could control my power, I could have...
                    case 0:
                        return 61;
                }
                return -1;
            case (61, 0):
                // $script:0727223007006874$
                // - ...saved him? Perhaps. The animus you possess was honed over centuries of training by one of the greatest masters Guidance had ever known.
                return 61;
            case (61, 1):
                // $script:0727223007006875$
                // - And if the master hadn't given you that animus, he may have had the power to stop this. I always feared something like this would happen...
                return 61;
            case (61, 2):
                // $script:0727223007006876$
                // - But... I suppose I can no longer humor such thoughts. It is just the three of us now.
                return 61;
            case (61, 3):
                // $script:0727223007006877$
                // - Losing him is... I don't...
                return 61;
            case (61, 4):
                // $script:0727223007006878$
                // - ...Well, you're his legacy now. Conduct yourself accordingly.
                switch (selection) {
                    // $script:0727223007006879$
                    // - I'll do my best.
                    case 0:
                        return 62;
                }
                return -1;
            case (62, 0):
                // $script:0727223007006880$
                // - Don't misunderstand me. I'm not trying to cheer you up.
                return 62;
            case (62, 1):
                // $script:0727223007006881$
                // - I don't like you, and I doubt I ever will. But, like it or not, you are my $male:brother,female:sister$ in Guidance. We must work together if we are to overcome our trials.
                switch (selection) {
                    // $script:0727233607006923$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.Next,
            (60, 1) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.Next,
            (61, 1) => NpcTalkButton.Next,
            (61, 2) => NpcTalkButton.Next,
            (61, 3) => NpcTalkButton.Next,
            (61, 4) => NpcTalkButton.SelectableDistractor,
            (62, 0) => NpcTalkButton.Next,
            (62, 1) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}
