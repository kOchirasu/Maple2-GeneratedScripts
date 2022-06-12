using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000552: Blackstar Gangster
/// </summary>
public class _11000552 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002337$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002338$
                // - If you've got business here, talk to a broker. Keep your hands to yourself. I'll be watching.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
