using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000629: Kimo
/// </summary>
public class _11000629 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002530$
    // - Screeeeech!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002532$
                // - $map:02000051$ is a great place to raise a family like mine. Its highlands are safe from monsters on the ground, and my children can practice flying!
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
