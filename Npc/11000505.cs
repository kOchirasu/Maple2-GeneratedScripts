using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000505: Blackstar Gangster
/// </summary>
public class _11000505 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0831180407002188$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002189$
                // - Scram, punk. 
                return -1;
            case (20, 0):
                // $script:0831180407002190$
                // - Who are you? Stop bothering me.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
