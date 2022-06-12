using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003958: Assassin
/// </summary>
public class _11003958 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614143707010007$
    // - ...What business do you have with me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614143707010008$
                // - ...You seem strong.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
