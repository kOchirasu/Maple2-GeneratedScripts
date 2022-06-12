using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003877: Loana
/// </summary>
public class _11003877 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0417135107009870$
    // - The waves are calm today! It's a nice day to go sailing.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0417135107009871$
                // - The waves are calm today! It's a nice day to go sailing.
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
