using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000107: Lucy
/// </summary>
public class _11000107 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407000438$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407000441$
                // - The Royal Road is blocked, and the forest path is too dangerous. I can't even go back home since the sea routes are messed up now too. I don't know what to do.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
