using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004260: Skate Fan
/// </summary>
public class _11004260 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011164$
    // - Stupid, stupid, stupid! Where is he?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011165$
                // - Stupid, stupid, stupid! Where is he?
                switch (selection) {
                    // $script:0911203207011166$
                    // - Where is who?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0911203207011167$
                // - Oh. Um. Just this guy who skateboards around here sometimes. He looks sooooo cool. I've been waiting for him.
                switch (selection) {
                    // $script:0911203207011168$
                    // - Oh, were you guys meeting up here? Is he late? Tsk, tsk.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0911203207011169$
                // - Um... I haven't actually officially met him yet. But that's what I've been waiting around for! I want to ask him for his name and number!
                return 12;
            case (12, 1):
                // $script:0911203207011170$
                // - Seriously, though, a girl's got limits. I've been waiting here every day for a week, and he hasn't showed up once! Now my legs hurt. Maybe I should give up.
                switch (selection) {
                    // $script:0911203207011171$
                    // - Aww, just wait a little longer. Never give up!
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:0911203207011172$
                // - Ugh, fine, I'll give him <b>one</b> more day. I mean, he is, like, super hot.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
