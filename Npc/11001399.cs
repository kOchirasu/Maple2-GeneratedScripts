using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001399: Grizzle
/// </summary>
public class _11001399 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217193307005399$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1228164407005733$
                // - After that red sandstorm, a weird ruin popped out from the dunes. I can't wait to see what kind of secrets it holds!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
