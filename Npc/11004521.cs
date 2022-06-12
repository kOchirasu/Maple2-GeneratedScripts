using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004521: Mayu
/// </summary>
public class _11004521 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0102174210002228$
    // - If you need a lift back to $map:02000001$, I'm your gal!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0102174210002229$
                // - If you need a lift back to $map:02000001$, I'm your gal!
                return 10;
            case (10, 1):
                // $script:0102174210002230$
                // - We're heading out straight away. If you miss this place, you can always use the <i>Lumiwind</i> to come back. Are you ready to return to $map:02000001$?
                switch (selection) {
                    // $script:0102174210002231$
                    // - Take me to $map:02000001$!
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0102174210002232$
                // - All right. Away we go!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
