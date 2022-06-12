using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004383: Judy
/// </summary>
public class _11004383 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011809$
    // - What kinda presents do you think Santa is bringing this year?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011810$
                // - What kinda presents do you think Santa is bringing this year?
                switch (selection) {
                    // $script:1109213607011811$
                    // - Do you think Santa is... real?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109213607011812$
                // - Seriously? You're gonna come to a festive place like this and ask THAT?
                switch (selection) {
                    // $script:1109213607011813$
                    // - I... well...
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109213607011814$
                // - Hey, I know the truth, but if I admit it I might get fewer presents. So yeah, go Santa!
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
