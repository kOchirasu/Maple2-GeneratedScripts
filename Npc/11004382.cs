using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004382: Lydia
/// </summary>
public class _11004382 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011803$
    // - I will find love this winter!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011804$
                // - I confessed my love to someone during the holidays last year...
                switch (selection) {
                    // $script:1109213607011805$
                    // - What happened?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109213607011806$
                // - The very next day, he gave it away. This year, I'll give it to someone special...
                switch (selection) {
                    // $script:1109213607011807$
                    // - Well, happy holidays!
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109213607011808$
                // - You listen to me, find your true love before the year ends!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
