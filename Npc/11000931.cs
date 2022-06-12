using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000931: Kaveki
/// </summary>
public class _11000931 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003305$
    // - It's too late for regrets...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003307$
                // - Sometimes I hate being able to see things that others can't.
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
