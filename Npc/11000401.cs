using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000401: Melson
/// </summary>
public class _11000401 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407001623$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001625$
                // - Please be very careful with this. It's one of my all-time favorite comic books.
                return -1;
            case (30, 0):
                // $script:0831180407001626$
                // - $male:Mister,female:Lady$, do you like comic books? They're my favorite thing in the world. I want to be an illustrator when I grow up.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
