using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000147: Benhurst
/// </summary>
public class _11000147 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000628$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000630$
                // - When will I ever have another chance to see the empress in person? I really want to go see the court!
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
