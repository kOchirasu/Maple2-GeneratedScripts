using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000424: Old Lady Balmony
/// </summary>
public class _11000424 : NpcScript {
    protected override int First() {
        return 60;
    }

    // Select 0:
    // $script:0831180407001767$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (60, 0):
                // $script:0831180407001771$
                // - Have you seen a lost, crying girl on the street? She's carrying a doll in her arms like it's a real baby.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
