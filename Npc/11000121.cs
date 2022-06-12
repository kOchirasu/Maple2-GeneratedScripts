using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000121: Daniel
/// </summary>
public class _11000121 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407000521$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407000526$
                // - Each of the monsters from the Land of Darkness has unique genetic material. By analyzing a wide range of material, I'm hoping to determine the rules that differentiate them from Maple World's monsters.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
