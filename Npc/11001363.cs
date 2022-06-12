using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001363: Mika
/// </summary>
public class _11001363 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1215222907005046$
    // - It's been too long since we gathered like this.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1230171207005753$
                // - You can return the necklace... later, and in person!
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
